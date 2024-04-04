
frappe.ready(function() {
	frappe.web_form.validate = () => {
		let data = frappe.web_form.get_values();
		if (data.flight_price <= 1000000) {
			frappe.msgprint('Value must be more than 1000');
			return false;
		}
	};


	// frappe.web_form.set_df_property([fieldname], [property], [value]);
	frappe.web_form.set_value("flight_price", "10000")
	frappe.web_form.set_df_property(["flight_price"], ["read_only"], ["1"]);
	console.log(frappe.web_form)
// })
})
