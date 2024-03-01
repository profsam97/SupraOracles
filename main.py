import subprocess
import sys
import pytest
from datetime import datetime

# Function to execute the test cases against the target software or application
def execute_test_cases(test_cases):
    try:
        # Run pytest tests
        pytest.main(test_cases)
    except Exception as e:
        print('Error executing test cases:', e)

# This is the function to generate a detailed report which highlights the pass/fail status of each test case
def generate_report():
    try:
        # Get the current date and time for report timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        report_file = f'Test_report_{timestamp}.html'
        
        # Run pytest with HTML report generation
        subprocess.call(['pytest', '-v', '--html=' + report_file])
        with open(report_file, 'a') as report:
            report.write("""
            <style>
            body {
                text-align: center;
            }
            h1 {
                font-size: 24px
                font-weight: bold
            }
            p {
                font-size: 18px
            }
            h2 {
                font-size: 20px
            }
            </style>
            """)
        
        print(f'Test execution completed successfully. Report generated: {report_file}')  
    except Exception as e:
        print('Error generating report:', e)

# Main function to orchestrate the test execution and report generation process
def main():
    test_cases_file = sys.argv[1] if len(sys.argv) > 1 else 'test_calculator.py'
    try:
        with open(test_cases_file, 'r') as file:
            test_cases = file.read().splitlines()
    except Exception as e:
        print(f'Error reading test cases from file: {e}')
        return

    # Execute test cases
    execute_test_cases(test_cases)

    # Generate report
    generate_report()

if __name__ == "__main__":
    main()
