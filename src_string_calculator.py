import re

class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiter = ','
        if numbers.startswith("//"):
            parts = numbers.split('\n', 1)
            delimiter = parts[0][2:]
            numbers = parts[1]
        
        numbers = re.split(f'{delimiter}|\n', numbers)
        numbers = [int(num) for num in numbers]

        negatives = [num for num in numbers if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")

        return sum(numbers)
