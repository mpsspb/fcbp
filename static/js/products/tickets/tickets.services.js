/**
* Tickets
* @namespace fcbp.layout.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.services')
    .factory('Tickets', Tickets);

  Tickets.$inject = ['$http'];

  /**
  * @namespace Tickets
  * @returns {Factory}
  */
  function Tickets($http) {
    /**
    * @name Tickets
    * @desc The Factory to be returned
    */
    var Tickets = {
      create: create,
      list: list,
      get: get,
      use: use,
      use_exit: use_exit,
      freeze: freeze,
      prolongation: prolongation,
      active: active,
      active_list: active_list,
      archive_client_list: archive_client_list,
};

    return Tickets;

    ////////////////////
    /**
    * @name create
    * @desc Create a new Tickets
    * @param {array} The form data of the new Tickets
    * @returns {Promise}
    * @memberOf fcbp.layout.services.Tickets
    */
    function create(fdata) {
      return $http.post('/api/v1/products/tickets/', fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list() {
      return $http.get('/api/v1/products/tickets/')
    }

    function active_list() {
      return $http.get('/api/v1/products/tickets/active_list/')
    }

    function get(uid) {
      return $http.get('/api/v1/clients/ticket/' + uid + '/')
    }

    function active(uid) {
      return $http.post('/api/v1/products/tickets/' + uid + '/active/')
    }

    function use(fdata) {
      return $http.post('/api/v1/clients/useticket/', fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }

    function use_exit(fdata) {
      return $http.post('/api/v1/clients/useticket/exit/', fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    };

    function freeze(uid, fdata) {
      return $http.post('/api/v1/clients/ticket/' + uid + '/freeze/', fdata)
    };

    function prolongation(fdata) {
      return $http.post('/api/v1/clients/prolongationticket/',  fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    };

    function archive_client_list(uid) {
      return $http.get('/api/v1/clients/archive/ticket/'+ uid + '/client/')
    };


  }

})();