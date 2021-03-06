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
    * @desc Create a new Period
    * @param {number} value The value of the new Period
    * @returns {Promise}
    * @memberOf fcbp.periods.services.Periods
    */
    function create(fdata) {
      return $http.post('/api/v1/products/periods/', fdata
                        ).error(function(data, status, headers, config) {
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