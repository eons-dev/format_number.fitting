import os
import logging
from pipeadapter import Fitting
from pipeadapter import OtherFittingError

class format_number(Fitting):
    def __init__(this, name="Format Number"):
        super().__init__(name)

        this.requiredKWArgs.append("value")
        this.requiredKWArgs.append("operation")

        this.optionalKWArgs["at"] = 2

    # Required Fitting method. See that class for details.
    def Run(this):
        if (this.operation == "insert_decimal"):
            valueStr = str(this.value)
            begin = valueStr[:int(f"-{this.at}")]
            end = valueStr[int(f"-{this.at}"):]
            valueStr = begin + "." + end
            this.output["value"] = float(valueStr)
        else:
            raise OtherFittingError(f"Operation {this.operation} not supported.")