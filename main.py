import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import os

from datetime import date, timedelta

from homebank_report.account import Account
from homebank_report.operation import Operation
from homebank_report.operation_set import OperationSet
from homebank_report.property import Property
from homebank_report.currency import Currency
from homebank_report.category import Category
from homebank_report.account_report import AccountReport
from homebank_report.date_utils import convert_date_from_homebank_format, convert_date_to_homebank_format
from homebank_report.pie_chart import generate_expenses_pie_chart, generate_revenue_pie_chart
from homebank_report.options import Options
from homebank_report.graph import generate_evolution_graph
from homebank_report.notifications.notifications import Notifications


class Period:

    start_date = None
    end_date = None
    name = None
    slug = None

    def __init__(self, name, start_date, end_date):
        self.name = name
        self.slug = name.lower().replace(' ', '_')
        self.start_date = start_date
        self.end_date = end_date


def process_file_contents(root, options):
    properties = Property(**root.find('properties').attrib)
    currencies = {currency.attrib['key']: Currency(**currency.attrib) for currency in root.findall('cur')}
    categories = {category.attrib['key']: Category(**category.attrib) for category in root.findall('cat')}

    # Create account instances and associate operations with accounts
    accounts = {account.attrib['key']: Account(**account.attrib) for account in root.findall('account')}
    operations = []

    for operation_elem in root.findall('ope'):
        operation_attribs = operation_elem.attrib
        account_key = operation_attribs['account']
        operation = Operation(**operation_attribs)
        account = accounts[account_key]
        account.operations.append(operation)
        operations.append(operation)

    last_month = Period(
        "Último mes",
        convert_date_to_homebank_format(date.today() - timedelta(days=30)),
        convert_date_to_homebank_format(date.today())
    )
    last_year = Period(
        "Último año",
        convert_date_to_homebank_format(date.today() - timedelta(days=365)),
        convert_date_to_homebank_format(date.today())
    )
    always = Period(
        "Siempre",
        0,
        convert_date_to_homebank_format(date.today())
    )
    for account in accounts.values():

        report = generate_account_report(last_month, account, categories, options)
        if (report):
            send_account_report(options, report)

        '''
        send_account_report(
            options,
            generate_account_report(last_month, account, categories, options)
        )

        send_account_report(
            options,
            generate_account_report(last_year, account, categories, options)
        )

        send_account_report(
            options,
            generate_account_report(always, account, categories, options)
        )
        '''

def main():
    options = Options(os.environ)

    try:
        tree = ET.parse(options.get("xml_file"))
        root = tree.getroot()
        process_file_contents(root, options)
    except ET.ParseError:
        print("Error: Invalid XML file")

def send_account_report(options, report):
    endpoint = options.get("notifications")[report.name]
    Notifications.send(endpoint, f"# {report.period.name} {report.name}: {report.balance}€")

    if (len(report.top_10) > 0):
        top_10 = f"## Top 10 Gastos:\n"
        for operation in report.top_10:
            info = operation.info if operation.info else ''
            wording = f" > {operation.wording}" if operation.wording else ''
            top_10 += f"- {info}{wording}: {operation.amount}€ \n"
        Notifications.send(endpoint, top_10)

    if (report.expenses_graph_path != ''):
        Notifications.send_file(endpoint, "## Tipo de gastos", report.expenses_graph_path)
    if (report.revenue_graph_path != ''):
        Notifications.send_file(endpoint, "## Tipo de ingresos", report.revenue_graph_path)
    if (report.evolution_graph_path != ''):
        Notifications.send_file(endpoint, "## Evolución", report.evolution_graph_path)

def generate_account_report(period, account, categories, options):
    operations = account.get_operation_set_between(period.start_date, period.end_date)
    if (len(operations) == 0):
        return None
    return AccountReport(
    name=account.name,
    period=period,
    balance=operations.get_balance(),
    expenses_graph_path=generate_expenses_pie_chart(
        account.name,
        options,
        categories,
        operations.get_expenses()
    ),
    revenue_graph_path=generate_revenue_pie_chart(
        account.name,
        options,
        categories,
        operations.get_revenues()
    ),
    evolution_graph_path=generate_evolution_graph(
        account.name,
        options,
        operations
    ),
    top_10=operations.get_top_10()
)


main()
