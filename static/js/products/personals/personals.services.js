/**
* Personals
* @namespace fcbp.layout.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.services')
    .factory('Personals', Personals);

  Personals.$inject = ['$http'];

  /**
  * @namespace Personals
  * @returns {Factory}
  */
  function Personals($http) {
    /**
    * @name Personals
    * @desc The Factory to be returned
    */
    var Personals = {
      create: create,
      list: list,
    };

    return Personals;

    ////////////////////
    /**
    * @name create
    * @desc Create a new Personal
    * @param {form data} by models of the new Personal
    * @returns {Promise}
    * @memberOf fcbp.personals.services.Personals
    */
    function create(fdata) {
      return $http.post('/api/v1/products/personal/', fdata
                        ).error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list() {
      return $http.get('/api/v1/products/personal/')
    }
  }

})();