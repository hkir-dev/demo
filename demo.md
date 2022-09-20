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

* How can I report possible bugs?
  * IRI key and url encoding.

## Limitations

* Docker based usage
* Cannot duplicate row
* If table has single row, cannot edit it (need to manually type: http://127.0.0.1:5004/bds_taxonomy/CCN202002013?view=form)
* Single value per cell (no '|' based multi-values)

## Installation

1- Clone the project
```
git clone https://github.com/hkir-dev/demo.git
```

2- Switch to working branch
```
cd demo
git checkout bican
```

3- Build docker image (in /demo folder)
```
docker build --quiet --tag odd:latest .
```

4- Process tables (src/tables) and initiate internal database (in /demo folder)
```
docker run --rm -it -p 5004:5000 -v $(pwd):/work -w /work odd:latest make load
```

5- Run nanobot as web application (in /demo folder)
```
docker run --rm -it -p 5004:5555 -v $(pwd):/work -w /work odd:latest ./run.py
```

6- Browse nanobot
```
http://127.0.0.1:5004/bds
```
