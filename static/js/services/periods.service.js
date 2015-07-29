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
      all: all,
      create: create,
      get: get
    };

    return Periods;

    ////////////////////

    /**
    * @name all
    * @desc Get all Periods
    * @returns {Promise}
    * @memberOf fcbp.periods.services.Periods
    */
    function all() {
      return $http.get('/api/v1/products/periods/');
    }


    /**
    * @name create
    * @desc Create a new Post
    * @param {string} content The content of the new Post
    * @returns {Promise}
    * @memberOf fcbp.periods.services.Periods
    */
    function create(content) {
      return $http.post('/api/v1/products/periods/', {
        content: content
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