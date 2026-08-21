import sys

class DataPipelineException(Exception):
    pass

class BasePipelineStep():
    def __init__(self, step_name: str, config: dict):
        self.step_name = step_name
        self.config = config
        
    def log_step(self, message: str):
        print(f"[{self.step_name.upper()}] {message}")

    def run(self):
        raise NotImplementedError("Class must be implemented")

class ExtractionStep(BasePipelineStep):
    def __init__(self, step_name: str, config: dict):
        BasePipelineStep.__init__(self, step_name, config)

    def run(self):
        self.log_step("Pulling raw partitions...")
        return {"records_extracted": 150}

class ValidationStep(BasePipelineStep):
    def __init__(self, strict_mode: bool, step_name: str, config: dict):
        self.strict_mode = strict_mode
        BasePipelineStep.__init__(self, step_name, config)

    def run(self):
        if self.strict_mode:
            self.log_step("Running strict validation....")
        else:
            self.log_step("Running standard validation....")       
        return {"status": "VALID"}

class FailingStep(BasePipelineStep):
    def __init__(self, step_name: str, config: dict):
        BasePipelineStep.__init__(self, step_name, config)
    def run(self):
        raise DataPipelineException("Warehouse connection timeout")

if len(sys.argv) < 2:
    print(f"[ERROR] please provide a step name: extract, validate or fail")
    sys.exit(1)

command = sys.argv[1].lower()
step_instance = None

if command == "extract":
    step_instance = ExtractionStep("extract", None)
elif command == "validate":
    step_instance = ValidationStep(True, "validate", None)
elif command == "fail":
    step_instance = FailingStep("fail", None)
else:
    print(f"[ERROR] Unkown step: '{command}'. Expected: extract, validate, fail")
    sys.exit(1)  

try:
    result = step_instance.run()
    print(f"[RUNNER] Step succeeded with output: {result}")
    sys.exit(0)

except DataPipelineException as e:
    print(f"[FATAL ERROR] {type(e).__name__}: {e}")
    sys.exit(2)

except Exception as e:
    print(f"[UNEXPECTED ERROR] {e}")
    sys.exit(1)



