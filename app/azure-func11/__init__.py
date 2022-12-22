import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, inputDocument: func.DocumentList) -> func.HttpResponse:

    userId = req.params.get('userId')

    if not inputDocument:
        logging.warning("item not found")
        return func.HttpResponse("item not found",status_code=200)
    else:
        logging.info("item found, Description=%s", len(inputDocument))

        for doc in inputDocument:
            #logging.info('Item Id: {0}'.format(doc.get('id')))
            #logging.info('Item Id: {0}'.format(doc.get('articles')))
            if doc.get('id') == userId:
                art = doc.get('articles')
                break

        result = json.dumps(art)

        return func.HttpResponse(result, mimetype="application/json",status_code=200)