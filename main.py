import unittest
import json
from mean_var_std import calculate
from test_module import TestMeanVarStd

# Example call
print("📊 Calculating Mean, Variance, and Standard Deviation...\n")
result = calculate([0,1,2,3,4,5,6,7,8])

# Pretty print output dictionary
print(json.dumps(result, indent=2))

print("\n🧪 Running Unit Tests...\n")
unittest.main(argv=[''], exit=False)
