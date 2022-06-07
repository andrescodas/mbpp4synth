def camel_to_snake(text):
        """
        Write a function to convert camel case string to snake case string.
        """
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
