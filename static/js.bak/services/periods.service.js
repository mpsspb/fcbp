/**
* Periods
* @namespace fcbp.periods.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.periods.services')
    .factory('Periods', Periods);

  Periods.$inject = ['$http'];

  /**
  * @namespace Periods
  * @returns {Factory}
  */
  function Periods($http) {
    var Periods = {
      list: list,
      create: create,
      get: get
    };

    return Periods;

    ////////////////////

    /**
    * @name list
    * @desc Get list Periods
    * @returns {Promise}
    * @memberOf fcbp.periods.services.Periods
    */
    function list() {
      return $http.get('/api/v1/products/periods/');
    }


    /**
    * @name create
    * @desc Create a new Post
    * @param {number} value The value of the new Period
    * @returns {Promise}
    * @memberOf fcbp.periods.services.Periods
    */
    function create(value) {
      return $http.post('/api/v1/products/periods/', {
        value: value
      }).error(function(data, status, headers, config) {
        console.log(data)
      });
    }

    /**
     * @name get
     * @desc Get the Period
     * @param {string} pid The pid to get Periods for
     * @returns {Promise}
     * @memberOf fcbp.periods.services.Periods
     */
    function get(pid) {
      return $http.get('/api/v1/products/periods/pid');
    }
  }
})();