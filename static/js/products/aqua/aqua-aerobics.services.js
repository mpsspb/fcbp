/**
* AquaAerobics
* @namespace fcbp.layout.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.services')
    .factory('AquaAerobics', AquaAerobics);

  AquaAerobics.$inject = ['$http'];

  /**
  * @namespace AquaAerobics
  * @returns {Factory}
  */
  function AquaAerobics($http) {
    /**
    * @name AquaAerobics
    * @desc The Factory to be returned
    */
    var AquaAerobics = {
      create: create,
      list: list,
      get: get,
      update: update,
      use:use,
      use_exit: use_exit,
      active: active,
      active_list: active_list,
      freeze: freeze,
    };

    return AquaAerobics;

    ////////////////////
    /**
    * @name create
    * @desc Create a new AquaAerobics
    * @param {array} The form data of the new AquaAerobics
    * @returns {Promise}
    * @memberOf fcbp.layout.services.AquaAerobics
    */
    function create(fdata) {
      return $http.post('/api/v1/products/aquaaerobics/', fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list() {
      return $http.get('/api/v1/products/aquaaerobics/')
    }

    function active_list() {
      return $http.get('/api/v1/products/aquaaerobics/active_list/')
    }

    function get(uid) {
      return $http.get('/api/v1/clients/aquaaerobics/' + uid + '/')
    }

    function update(uid, fdata) {
      return $http.put('/api/v1/products/aquaaerobics/' + uid + '/', fdata)
    }

    function active(uid) {
      return $http.post('/api/v1/products/aquaaerobics/' + uid + '/active/')
    }

    function use(fdata) {
      return $http.post('/api/v1/clients/useaquaaerobics/', fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }

    function use_exit(fdata) {
      return $http.post('/api/v1/clients/useaquaaerobics/exit/', fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    };

    function freeze(uid, fdata) {
      return $http.post('/api/v1/clients/aquaaerobics/' + uid + '/freeze/', fdata)
    };

  };

})();