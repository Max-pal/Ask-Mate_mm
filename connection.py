from flask import Flask, render_template, request, redirect


def descending_sort_data_by_parameter(data_to_be_sorted, parameter):
    sorted_data = []
    sorted_data = sorted(data_to_be_sorted, key=lambda k: k[parameter], reverse=True)
    return sorted_data
