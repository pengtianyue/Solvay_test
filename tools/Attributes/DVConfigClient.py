'''
Module contains client definitions to get DeltaV configuration data from a DVConfigServer
'''

import jsocket
import time


class DVConfigClient(jsocket.JsonClient):

    def __init__(self, address='127.0.0.1', port=5489):
        self.address = address
        self.port = port
        super(DVConfigClient, self).__init__(address=address, port=port)
        print address, port

        if address:
            self.address = address

        if port:
            self.port = port

    def disconnect(self):
        self.close()

    def set_server(self, address=None, port=None):
        if address:
            self.address = address
        if port:
            self.port = port

    def get_module_info(self, tag):
        '''
        Returns dictionary of information about DeltaV module
        :param tag: reference tag of module query
        :return: dictionary
        '''
        rpc_req = {
            "method": "get_module_info",
            "tag": tag
                   }

        self.send_obj(rpc_req)
        info = self.read_obj()
        return info

    def get_alias(self, tag, alias):
        '''
        Returns dictionary of information resolving alias
        :param tag:
        :param alias:
        :return:
        '''
        rpc_req = {
            "method": "get_alias",
            "tag": tag,
            "reference_id": alias
        }

        self.send_obj(rpc_req)
        info = self.read_obj()
        return info

    def get_namedset(self, namedset_name):
        '''
        Returns a dictionary of a namedset's entry {string value: integer value} map
        :param namedset_name: string name of desired namedset
        :return:
        '''
        rpc_req = {
            "method": "get_namedset",
            "namedset": "namedset_name"
        }
        self.send_obj(rpc_req)
        info = self.read_obj()
        return info

    def get_config_values(self, list_of_paths):
        '''
        Returns the configuration values found for each of the paths in list_of_paths
        :param list_of_paths:
        :return:
        '''

        if type(list_of_paths) is not list:
            print "Must pass a list of paths to query. Received type:", type(list_of_paths)
            raise TypeError

        rpc_req = {
            "method": "get_config_values",
            "path_values": list_of_paths,
        }
        self.send_obj(rpc_req)
        info = self.read_obj()
        return info


if __name__ == "__main__":
    client = DVConfigClient()

    client.connect()

    client.get_module_info('CV-4148')
    time.sleep(1)
    client.get_alias('R3-PRES-EM', 'ATM_VENT_VLV')
    time.sleep(1)

