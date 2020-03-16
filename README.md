# Inventory Management 

A django application for inventory management

Source Code:
------------

`<https://github.com/BHushanRathod/flask_demo.git>`_


Installation and Usage
======================

Download the souce code::
       
    $ git clone https://github.com/BHushanRathod/flask_demo.git
   
Activate the Virtual Environment::

    source ~/path/to/ve/bin/activate

Install the Dependencies::

    pip install -r requirements.txt

Run server::
    
    python app.py
    
* Steps to follow:
    * open browser, with following url
    
            http://localhost:5000/
            
    * For reading file1.txt, with start line = 1 and end line 10, hit with GET call (provide start and end querystring)
    
            http://localhost:5000/?start=1&end=10&file=file1
            
    * For reading file4, hit with GET call
    
            http://localhost:5000/?file=file4
            