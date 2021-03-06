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
      update: update,
      introductory: introductory,
      online: online,
      search: search,
      full_search: full_search,
      exact_search: exact_search,
      advanced_search: advanced_search,
      last_clubcard: last_clubcard,
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

    function update(fdata, uid) {
      return $http.put('/api/v1/clients/client/' + uid + '/', fdata)
    }

    function introductory(uid, fdata) {
      return $http.post('/api/v1/clients/client/' + uid + '/introductory/',
        fdata)
    }

    function online() {
      return $http.get('/api/v1/clients/client/online/');
    }

    function search(fdata) {
      return $http.post('/api/v1/clients/client/search/', fdata);
    }

    function full_search(fdata) {
      return $http.post('/api/v1/clients/client/full_search/', fdata);
    }

    function exact_search(fdata) {
      return $http.post('/api/v1/clients/client/exact_search/', fdata);
    }

    function advanced_search(fdata) {
      return $http.get('/api/v1/clients/advanced_search/', fdata);
    }

    function last_clubcard(uid, fdata) {
      return $http.get('/api/v1/clients/client/' + uid + '/last_clubcard/')
    };

  }

})();