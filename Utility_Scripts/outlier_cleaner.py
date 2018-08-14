#!/usr/bin/python
import numpy

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    residual_errors = (predictions - net_worths)
    outlier_threshold = numpy.percentile(numpy.absolute(residual_errors),90)
    
    cleaned_data = [(age, net_worth, residual_error) for age, net_worth, 
                    residual_error in  zip(ages, net_worths, residual_errors)
                    if abs(residual_error) <= outlier_threshold]
    

  
    return cleaned_data

