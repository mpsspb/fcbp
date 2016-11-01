/**
* ClientCredit
* @namespace fcbp.clients.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.services')
    .factory('ClientCredit', ClientCredit);

  ClientCredit.$inject = ['$http'];

  /**
  * @namespace ClientCredit
  * @returns {Factory}
  */
  function ClientCredit($http) {
    /**
    * @name ClientCredit
    * @desc The Factory to be returned
    */
    var ClientCredit = {
      create: create,
      list: list,
      update: update,
    };

    return ClientCredit;

    ////////////////////
    /**
    * @name create
    * @desc Create a new ClientCredit
    * @param {array} The form data of the new ClientCredit
    * @returns {Promise}
    * @memberOf fcbp.clients.services.ClientCredit
    */
    function create(fdata) {
      return $http.post('/api/v1/finance/credits/', fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list(page, letter) {
      return $http.get('/api/v1/finance/credits/', 
                        {params: {page: page,
                                  letter: letter} })
    }

    function update(uid, fdata) {
      return $http.put('/api/v1/finance/credits/' + uid + '/', fdata)
    }

  }

})();