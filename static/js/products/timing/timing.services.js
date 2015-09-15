/**
* Tickets
* @namespace fcbp.layout.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.services')
    .factory('Timing', Timing);

  Timing.$inject = ['$http'];

  /**
  * @namespace Timing
  * @returns {Factory}
  */
  function Timing($http) {
    /**
    * @name Timing
    * @desc The Factory to be returned
    */
    var Timing = {
      create: create,
      list: list,
      get: get,
      use: use,
    };

    return Timing;

    ////////////////////
    /**
    * @name create
    * @desc Create a new Timing
    * @param {array} The form data of the new Timing
    * @returns {Promise}
    * @memberOf fcbp.layout.services.Timing
    */
    function create(fdata) {
      return $http.post('/api/v1/products/timing/', fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list() {
      return $http.get('/api/v1/products/timing/')
    }

    function get(uid) {
      return $http.get('/api/v1/clients/timing/' + uid + '/')
    }

    function use(fdata) {
      return $http.post('/api/v1/clients/usetiming/',  fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }  

  }

})();