""" Utilities module of static methods """
class Utils(object):
    """Utilities class """

    @staticmethod
    def clamp(number, minn, maxn):
        """ ensures integer stays within range """
        return max(min(maxn, number), minn)

    @staticmethod
    def parse_bool(source):
        """ parses non boolean values into boolean results """
        return bool(source.lower() in ['true', '1', 't', 'y', 'yes'])

    @staticmethod
    def status(source, form):
        """ will convert from multiple status formats into a specified format """
        if source is not None and form is not None:
            cross_walk_from = {
                'O'  : 0, 'FAIL':0, 'OPEN': 0, 'ONGOING' : 0,
                'NR' : 1, 'NOT_REVIEWED' : 1, 'NOT REVIEWED' : 1,
                'NA' : 2, 'NOTAPPLICABLE': 2, 'NOT_APPLICABLE': 2, 'NOT APPLICABLE' : 2,
                'C'  : 3, 'NOTAFINDING': 3, 'CLOSED' : 3, 'PASS' : 3, 'COMPLETED' : 3,
                'E'  : 4, 'ERROR' : 4
            }
            cross_walk_to = {
                'ABBREV' : {0: 'O', 1: 'NR', 2: 'NA', 3: 'C', 4: 'E'},
                'HUMAN' : {
                    0: 'Open', 1: 'Not Reviewed', 2: 'Not Applicable', 3: 'Closed', 4: 'Error'
                },
                'RAW' : {
                    0: 'Open', 1: 'Not_Reviewed', 2: 'Not_Applicable', 3: 'Closed', 4: 'Error'
                },
            }
            return cross_walk_to[form][cross_walk_from[str(source).upper().strip()]]
        return 'Status Unknown'

    @staticmethod
    def risk_val(source, form):
        """ will convert from multiple risk formats into a specified format """
        if source is not None and form is not None:
            cross_walk_from = {
                '' : 0, 'UNKNOWN':0,
                'VL': 0, 'L': 1, 'M': 2, 'H': 3, 'VH': 4,
                'NONE': 0, 'INFO': 0, 'LOW': 1, 'MEDIUM': 2, 'HIGH': 3,
                'CRITICAL': 4, 'VERY HIGH' : 4,
                'CATIV': 0, 'CATIII': 1, 'CATII': 2, 'CATI': 3,
                'IV': 0, 'III': 1, 'II': 2, 'I': 3,
                'CAT IV': 0, 'CAT III': 1, 'CAT II': 2, 'CAT I': 3,
                'MODERATE': 2, 0: 0, 1: 1, 2: 2, 3: 3, 4: 4,
                '0':0, '1':1, '2':2, '3':3, '4':4
            }

            cross_walk_to = {
                'VL-VH': {
                    0: 'VL', 1: 'L', 2: 'M', 3: 'H', 4: 'VH',
                },
                'VL VH': {
                    0: 'Very Low', 1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High',
                },
                'POAM': {
                    0: 'Very Low', 1: 'Low', 2: 'Moderate', 3: 'High', 4: 'Very High',
                },
                'N-C': {
                    0: 'None', 1: 'Low', 2: 'Medium', 3: 'High', 4: 'Critical',
                },
                'CAT': {
                    0: 'CAT IV', 1: 'CAT III', 2: 'CAT II', 3: 'CAT I', 4: 'CAT I',
                },
                'MIN': {
                    0: 'IV', 1: 'III', 2: 'II', 3: 'I', 4: 'I',
                },
                'NUM':{
                    0: 0, 1: 1, 2: 2, 3: 3, 4: 4,
                },
            }

            return cross_walk_to[form][cross_walk_from[str(source).upper().strip()]]
        return 'Risk Unknown'
