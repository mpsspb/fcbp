/**
* Sports
* @namespace fcbp.layout.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.services')
    .factory('Sports', Sports);

  Sports.$inject = ['$http'];

  /**
  * @namespace Sports
  * @returns {Factory}
  */
  function Sports($http) {
    /**
    * @name Sports
    * @desc The Factory to be returned
    */
    var Sports = {
      create: create,
      list: list,
    };

    return Sports;

    ////////////////////
    /**
    * @name create
    * @desc Create a new Sport
    * @param {form data} by models of the new Sport
    * @returns {Promise}
    * @memberOf fcbp.sports.services.Sports
    */
    function create(fdata) {
      return $http.post('/api/v1/products/sports/', fdata
                        ).error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list() {
      return $http.get('/api/v1/products/sports/')
    }
  }

})();