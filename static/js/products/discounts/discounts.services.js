/**
* Discounts
* @namespace fcbp.layout.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.services')
    .factory('Discounts', Discounts);

  Discounts.$inject = ['$http'];

  /**
  * @namespace Discounts
  * @returns {Factory}
  */
  function Discounts($http) {
    /**
    * @name Discounts
    * @desc The Factory to be returned
    */
    var Discounts = {
      create: create,
      list: list,
      update: update,
    };

    return Discounts;

    ////////////////////
    /**
    * @name create
    * @desc Create a new Discount
    * @param {form data} by models of the new Discount
    * @returns {Promise}
    * @memberOf fcbp.Discounts.services.Discounts
    */
    function create(fdata) {
      return $http.post('/api/v1/products/discount/', fdata
                        ).error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list() {
      return $http.get('/api/v1/products/discount/')
    }

    function update(id, fdata) {
      return $http.put('/api/v1/products/discount/' + id + '/', fdata
                        ).error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
  }

})();