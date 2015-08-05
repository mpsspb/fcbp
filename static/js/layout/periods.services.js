/**
* Periods
* @namespace fcbp.layout.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.services')
    .factory('Periods', Periods);

  Periods.$inject = ['$http'];

  /**
  * @namespace Periods
  * @returns {Factory}
  */
  function Periods($http) {
    /**
    * @name Periods
    * @desc The Factory to be returned
    */
    var Periods = {
      create: create,
      list: list,
    };

    return Periods;

    ////////////////////
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
    **/
    function list() {
      return $http.get('/api/v1/products/periods/')
    }
  }

})();