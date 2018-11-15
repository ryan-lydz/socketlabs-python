from .addressresult import AddressResult
from .sendresult import SendResult


class SendResponse(object):
    """
    The response of an SocketLabsClient send request.
    """

    def __init__(self, result: SendResult = None, address_results: list = None, transaction_receipt: str = None):
        """
        Initializes a new instance of the SendResponse class
        :param result: the SendResult enum for the response
        :type result: SendResult
        :param address_results: the AddressResult list for the response
        :type address_results: list
        :param transaction_receipt: The unique key generated by the Injection API for the response
        :type transaction_receipt: str
        """
        self._result = result
        if address_results is not None:
            self._address_results = address_results
        else:
            self._address_results = []
        self._transaction_receipt = transaction_receipt

    @property
    def result(self):
        """
        Get the result of the SocketLabsClient send request.
        :return the result
        :rtype SendResult
        """
        return self._result

    @result.setter
    def result(self, val: SendResult):
        """
        Set the result of the SocketLabsClient send request.
        :param val: the SendResult
        :type val: SendResult
        """
        self._result = val

    @property
    def transaction_receipt(self):
        """
        Get the unique key generated by the Injection API if an unexpected error
        occurs during the SocketLabsClient send request.
        This unique key can be used by SocketLabs support to troubleshoot the issue.
        :return the list of transaction_receipt
        :rtype str
        """
        return self._transaction_receipt

    @transaction_receipt.setter
    def transaction_receipt(self, val: str):
        """
        Set the unique key generated by the Injection API if an unexpected error
        occurs during the SocketLabsClient send request.
        This unique key can be used by SocketLabs support to troubleshoot the issue.
        :param val: the transaction_receipt
        :type val: str
        """
        self._transaction_receipt = val

    @property
    def address_results(self):
        """
        Get a list of AddressResult objects that contain the status of each address
        that failed. If no messages failed this array is empty.
        :return the list of AddressResult
        :rtype list
        """
        return self._address_results

    @address_results.setter
    def address_results(self, val: list):
        """
        Set an array of AddressResult objects that contain the status of each address
        that failed. If no messages failed this array is empty.
        :param val: the list of AddressResult
        :type val: list
        """
        self._address_results = []
        if val is not None:
            for item in val:
                if isinstance(item, AddressResult):
                    self._address_results.append(item)

    @property
    def response_message(self):
        """
        A message detailing why the SocketLabsClient send request failed.
        :return the response_message
        :rtype str
        """
        return str(self._result)

    def __str__(self):
        """
        Represents the SendResponse as a str.
        :return the string
        :rtype str
        """
        return "{result}: {response_message}" \
            .format(
                result=self._result,
                response_message=self.response_message)

    def to_json(self):
        """
        build json dict for SendResponse
        :return the json dictionary
        :rtype dict
        """
        json = {
            "result": self._result.name,
            "transactionReceipt": self._transaction_receipt,
            "responseMessage": self.response_message
        }

        if len(self._address_results) > 0:
            e = []
            for a in self._address_results:
                e.append(a.to_json())
            json["messageResults"] = e
        return json