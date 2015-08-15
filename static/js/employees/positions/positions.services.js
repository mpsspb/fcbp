/**
* Positions
* @namespace fcbp.employees.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.employees.services')
    .factory('Positions', Positions);

  Positions.$inject = ['$http'];

  /**
  * @namespace Positions
  * @returns {Factory}
  */
  function Positions($http) {
    /**
    * @name Positions
    * @desc The Factory to be returned
    */
    var Positions = {
      create: create,
      list: list,
    };

    return Positions;

    ////////////////////
    /**
    * @name create
    * @desc Create a new Period
    * @param {number} value The value of the new Period
    * @returns {Promise}
    * @memberOf fcbp.employees.services.Positions
    */
    function create(fdata) {
      return $http.post('/api/v1/employees/positions/', fdata
                        ).error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list() {
      return $http.get('/api/v1/employees/positions/')
    }
  }

})();