/**
* ClientPayment
* @namespace fcbp.clients.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.services')
    .factory('ClientPayment', ClientPayment);

  ClientPayment.$inject = ['$http'];

  /**
  * @namespace ClientPayment
  * @returns {Factory}
  */
  function ClientPayment($http) {
    /**
    * @name ClientPayment
    * @desc The Factory to be returned
    */
    var ClientPayment = {
      create: create,
      list: list,
      close_credit: close_credit,
    };

    return ClientPayment;

    ////////////////////
    /**
    * @name create
    * @desc Create a new ClientPayment
    * @param {array} The form data of the new ClientPayment
    * @returns {Promise}
    * @memberOf fcbp.clients.services.ClientPayment
    */
    function create(fdata) {
      return $http.post('/api/v1/finance/payments/', fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list(page, letter) {
      return $http.get('/api/v1/finance/payments/', 
                        {params: {page: page,
                                  letter: letter} })
    }

    function close_credit(payment_type, uid) {
      return $http.post('/api/v1/finance/credits/' + uid + '/close/', 
                        {'payment_type': payment_type})
    }

  }

})();