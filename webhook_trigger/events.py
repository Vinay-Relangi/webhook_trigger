import frappe
import json
import requests

EXTERNAL_API_URL = "http://35.200.224.173/webhook"

def call_webhook(event, doc):
    try:
        payload = {
            "event": event,
            "doctype": doc.doctype,
            "docname": doc.name,
            "data": doc.as_dict()
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(EXTERNAL_API_URL, data=json.dumps(payload), headers=headers)
        if not response.ok:
            frappe.log_error(f"Webhook failed: {response.text}", f"Webhook Error ({event})")
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), f"Webhook Exception ({event})")

def handle_after_insert(doc, method=None): call_webhook("after_insert", doc)
def handle_before_save(doc, method=None): call_webhook("before_save", doc)
def handle_after_save(doc, method=None): call_webhook("after_save", doc)
def handle_on_update(doc, method=None): call_webhook("on_update", doc)
def handle_before_submit(doc, method=None): call_webhook("before_submit", doc)
def handle_on_submit(doc, method=None): call_webhook("on_submit", doc)
def handle_before_cancel(doc, method=None): call_webhook("before_cancel", doc)
def handle_on_cancel(doc, method=None): call_webhook("on_cancel", doc)
def handle_before_trash(doc, method=None): call_webhook("before_trash", doc)
def handle_on_trash(doc, method=None): call_webhook("on_trash", doc)
def handle_after_delete(doc, method=None): call_webhook("after_delete", doc)
def handle_on_rename(doc, method=None): call_webhook("on_rename", doc)
def handle_on_change(doc, method=None): call_webhook("on_change", doc)
def handle_validate(doc, method=None): call_webhook("validate", doc)