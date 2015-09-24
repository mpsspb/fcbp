/**
* Clients
* @namespace fcbp.clients.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.services')
    .factory('Clients', Clients);

  Clients.$inject = ['$http'];

  /**
  * @namespace Clients
  * @returns {Factory}
  */
  function Clients($http) {
    /**
    * @name Clients
    * @desc The Factory to be returned
    */
    var Clients = {
      create: create,
      list: list,
      get: get,
      introductory: introductory,
    };

    return Clients;

    ////////////////////
    /**
    * @name create
    * @desc Create a new Clients
    * @param {array} The form data of the new Clients
    * @returns {Promise}
    * @memberOf fcbp.clients.services.Clients
    */
    function create(fdata) {
      return $http.post('/api/v1/clients/client/', fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list(page, letter) {
      return $http.get('/api/v1/clients/client/', 
                        {params: {page: page,
                                  letter: letter} })
    }

    function get(uid) {
      return $http.get('/api/v1/clients/client/' + uid + '/')
    }

    function introductory(uid, fdata) {
      return $http.post('/api/v1/clients/client/' + uid + '/introductory/',
        fdata)
    }
  }

})();