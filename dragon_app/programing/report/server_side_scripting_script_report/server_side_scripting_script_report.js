// Copyright (c) 2022, MUHAMMED and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Server side scripting Script Report"] = {
	"filters": [
		{
			"fieldname": "name",
			"label":__("Server side scripting"),
			"fieldtype":"Link",
			"options":"Server side scripting"
		},
		{
			"fieldname": "dob",
			"label":__("DOB"),
			"fieldtype":"Date",

		},
		{
			"fieldname": "age",
			"label":__("Age"),
			"fieldtype":"Data",
		}

	]
};
