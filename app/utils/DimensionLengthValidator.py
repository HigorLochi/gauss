from app.variables.systemMaximumLength import maximumLength

class DimensionLengthValidator:
    def validate(self, rows, columns):
        if rows <= maximumLength and columns <= maximumLength:
            return True
        else:
            return False

    