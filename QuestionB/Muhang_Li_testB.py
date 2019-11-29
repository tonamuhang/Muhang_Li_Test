
class VersionComparor:

    @staticmethod
    def parse_version(version):
        version = list(map(int, version.split('.')))

        for i in version:
            if i < 0:
                raise ValueError("ValueError: Input version can't be negative")

        return version

    @staticmethod
    def compare_digits(v1, v2):
        for x, y in zip(v1, v2):
            x = str(x)
            y = str(y)

            difference = len(x) - len(y)
            if difference > 0:
                for i in range(difference):
                    y += "0"
            else:
                for i in range(-difference):
                    x += "0"

            x = int(x)
            y = int(y)
            if x > y:
                return 1
            elif x < y:
                return -1

        return 0


    @staticmethod
    def greater_than(version_1, version_2):
        version_1 = VersionComparor.parse_version(version_1)
        version_2 = VersionComparor.parse_version(version_2)

        if VersionComparor.compare_digits(version_1, version_2) == 1:
            return True

        return False

    @staticmethod
    def equals_to(version_1, version_2):
        version_1 = VersionComparor.parse_version(version_1)
        version_2 = VersionComparor.parse_version(version_2)

        if VersionComparor.compare_digits(version_1, version_2) == 0:
            return True

        return False

    @staticmethod
    def less_than(version_1, version_2):
        version_1 = VersionComparor.parse_version(version_1)
        version_2 = VersionComparor.parse_version(version_2)

        if VersionComparor.compare_digits(version_1, version_2) == -1:
            return True

        return False

