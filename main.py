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

    today = convert_date_to_homebank_format(date.today())
    last_month = convert_date_to_homebank_format(date.today() - timedelta(days=30))
    #last_year = convert_date_to_homebank_format(date.today() - timedelta(days=365))
    generate_account_reports(last_month, today, accounts, categories, options)
    #generate_account_reports(0, today)
    #generate_account_reports(last_year, today)

def main():
    options = Options(os.environ)

    try:
        tree = ET.parse(options.get("xml_file"))
        root = tree.getroot()
        process_file_contents(root, options)
    except ET.ParseError:
        print("Error: Invalid XML file")




def generate_account_reports(start_date, end_date, accounts, categories, options):
    for account in accounts.values():
        print(f"Account: {account.name}")
        operations = account.get_operation_set_between(start_date, end_date)
        print(f"Balance: {operations.get_balance()}")
        report = AccountReport(
            name=account.name,
            balance=operations.get_balance(),
            expenses_graph_path=generate_expenses_pie_chart(account.name, options, categories, operations.get_expenses()),
            revenue_graph_path=generate_revenue_pie_chart(account.name, options, categories, operations.get_revenues()),
            evolution_graph_path=generate_evolution_graph(account.name, options, operations)
        )
        for operation in operations.get_top_10():
            info = operation.info if operation.info else ''
            wording = operation.wording if operation.wording else ''
            print(f"{operation.amount}€ - {info}:{wording}")

main()
