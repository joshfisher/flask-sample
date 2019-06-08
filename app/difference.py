import datetime
from flask import request, jsonify
from .util import isnatural, fmt_date
from . import database

def handler():	
    try:
        input = request.args["number"]
        if not isnatural(input):
            raise ValueError()		
        num = int(input)		
        if 0 >= num or num > 100:
            raise ValueError()		
    except KeyError:		
        return (		
            'Missing input - "number" is required and must be a real number 1 - 100',		
            400,		
            [],		
        )		
    except ValueError:		
        return ('Invalid input - "number" must be a real number 1 - 100', 400, [])		

    sqr_sum = 0		
    sum = 0		
    for i in range(1, num + 1):		
        sqr_sum = sqr_sum + (i ** 2)		
        sum = sum + i		

    diff = (sum ** 2) - sqr_sum		

    cnt = database.incr_difference_request_count(num)		

    return jsonify(
        {
            "datetime": fmt_date(datetime.datetime.now()),		
            "value": diff,		
            "number": num,		
            "occurrences": cnt,		
        }		
    )		
