from flask import Blueprint, jsonify, request
from api.models import WordSearch
from sqlalchemy.sql.expression import func

utils = Blueprint('utils', __name__)

results = {
    'code': 0,
    'message': "Failure",
}


@utils.route("/search", methods=['GET'])
def words():
    try:
        return_data_arr = []
        word = request.args.get('word')
        words = WordSearch.query.filter(WordSearch.word.like("%" + word + "%")) \
            .order_by(func.length(WordSearch.word),
                      WordSearch.frequency.desc()) \
            .limit(25).all()
        if len(words) > 1:
            return_data_arr = [i.serialize for i in words]
            results['code'] = 1
            results['message'] = "success"
            results['count'] = len(words)
            results['data'] = return_data_arr
        return jsonify(results=results)
    except Exception:
        return jsonify(results=results)


@utils.route("/")
def home():
    results['code'] = 1
    results['message'] = "success"
    results['data'] = """
        Try searching words.Api url endpoint = '/search?word=pro'"""

    # # try:
    # objects = []
    # with open("word_search.tsv") as f:
    #     for line in f:
    #         lineData = line.split('\t')
    #         word = WordSearch(word=lineData[0], frequency=lineData[1][:-1])
    #         objects.append(word)
    # db.session.add_all(objects)
    # db.session.commit()
    #
    # results['code'] = 1
    # results['message'] = "success"
    # results['data'] = "success : {}".format(len(objects))
    # # except Exception:
    # #     return False

    return jsonify(results=results)
