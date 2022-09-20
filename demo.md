## TODO

* Create a BDS related table
* Load bds ontology
* Make row updating form editable (load from source)
* Attach autocomplete service to the form fields based on field type
* Deploy demo
* Auto complete service for CL 
* Auto complete service for Uberon

## Questions?

* Where is the edit template?
  * /nanobot/run.py  render_row_from_database  and  get_row_as_form  -> get_hiccup_form_row
* Dependency path to the edit file's project.
  * Docker nanobot clone
* xxxx Can datatype be used to extend the representation in edit file?
  * Where is the datatype - html type mapping
* How to configure endpoint, ontology etc.?

* How can I report possible bugs?
  * IRI key and url encoding.

## Limitations

* Docker based usage
* Cannot duplicate row
* Single value per cell (no '|' based multi-values)