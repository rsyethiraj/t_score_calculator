import argparse
import sys
import math
import typing

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list_values', action='store_true', help='If set, uses lists of data to parse information instead of single values')
    parser.add_argument('-b', '--in_lbs', action='store_true', help='If set, the weight values will be interpreted as being in lbs, otherwise, they will be treated as in kgs.')
    parser.add_argument('-w', '--weights', nargs = '+', help='The weights used to compute the T scores')
    parser.add_argument('-s', '--speeds', nargs='+', help='The speeds used to compute the T scores. Either in watts or splits')
    parser.add_argument('-n', '--names', nargs='*', help='If provided, will attach names to the resulting T scores. Optional.')
    args= parser.parse_args()
    if len(args.weights) != len(args.speeds):
        raise ValueError('The same number of weights and speeds must be provided.')
    if args.names is not None and len(args.names) != len(args.weights):
        raise ValueError('The same number of weights and names must be provided.')

    return args

def calculate_t_scores(weights: typing.List[float], watts: typing.List[float], names = None):
    #This method assumes that all weights passed in are already converted to kilograms.
    adjusted_weights = [i ** 0.667 for i in weights]
    t_scores = []
    for i in range(len(adjusted_weights)):
        t_scores.append(watts[i]/adjusted_weights[i])
        #Truncates the values to the first significant figure
        t_scores[i] = t_scores[i]*10 // 1 / 10
        if names is not None:
            t_scores[i] = names[i] + ': ' + str(t_scores[i])
    return t_scores
    
def split_to_watts(a: str):
    vals = a.split(':')
    mins, secs = int(vals[0]), int(vals[1].split('.')[0])
    dec = 0
    if len(vals[1].split('.')) > 1:
        dec = float(vals[1].split('.')[1])*0.1
    #Converts split into seconds/500m 
    t = (float(mins*60 + secs) + dec)/500
    # This is the formula used by Concept2 to convert seconds/500m into watts. The '*10 //1 / 10' block truncates the answer to one decimal place. 
    return (2.8 / t**3)*10 // 1 / 10
    
def main(args: argparse.Namespace):
    #convert splits to watts if necessary, convert all values to floats
    for i in range(len(args.speeds)):
        val = args.speeds[i]
        if len(val.split(':')) > 1:
            args.speeds[i] = split_to_watts(val)
        else:
            args.speeds[i] = float(args.speeds[i])
    #Converts all weight to kilograms
    if args.in_lbs:
        args.weights = [float(i) / 2.2 for i in args.weights]
    print(calculate_t_scores(args.weights, args.speeds, args.names))
    return 0
    
def start_script():
    try:
        pargs = parse_args()
    except(argparse.ArgumentError, ValueError, TypeError) as e:
        print('Argument Parsing error: ' + str(e))
        sys.exit(1)
    main(pargs)

if __name__ == '__main__':
    start_script()

