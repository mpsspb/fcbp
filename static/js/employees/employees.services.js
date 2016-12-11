/**
* Employees
* @namespace fcbp.employees.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.employees.services')
    .factory('Employees', Employees);

  Employees.$inject = ['$http'];

  /**
  * @namespace Employees
  * @returns {Factory}
  */
  function Employees($http) {
    /**
    * @name Employees
    * @desc The Factory to be returned
    */
    var Employees = {
      create: create,
      list: list,
      get: get,
      edit: edit,
      sellers: sellers,
      active: active,
    };

    return Employees;

    ////////////////////
    /**
    * @name create
    * @desc Create a new Period
    * @param {number} value The value of the new Period
    * @returns {Promise}
    * @memberOf fcbp.employees.services.Employees
    */
    function create(fdata) {
      return $http.post('/api/v1/employees/employees/', fdata
                        ).error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list(all=false) {
      if (all) {
        return $http.get('/api/v1/employees/employees/all/')        
      } else {
        return $http.get('/api/v1/employees/employees/')
      }
    }
    function get(uid) {
      return $http.get('/api/v1/employees/employees/' + uid + '/')
    }
    function edit(uid, fdata) {
      return $http.put('/api/v1/employees/employees/' + uid + '/',
        fdata).error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    function active(uid) {
      return $http.post('/api/v1/employees/employees/' + uid + '/active/')
    }
    // only employees who is seller
    function sellers() {
      return $http.get('/api/v1/employees/employees/sellers/')
    }

  }

})();