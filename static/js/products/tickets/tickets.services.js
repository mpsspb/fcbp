/**
* Tickets
* @namespace fcbp.layout.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.services')
    .factory('Tickets', Tickets);

  Tickets.$inject = ['$http'];

  /**
  * @namespace Tickets
  * @returns {Factory}
  */
  function Tickets($http) {
    /**
    * @name Tickets
    * @desc The Factory to be returned
    */
    var Tickets = {
      create: create,
      list: list,
    };

    return Tickets;

    ////////////////////
    /**
    * @name create
    * @desc Create a new Tickets
    * @param {array} The form data of the new Tickets
    * @returns {Promise}
    * @memberOf fcbp.layout.services.Tickets
    */
    function create(fdata) {
      return $http.post('/api/v1/products/tickets/', fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list() {
      return $http.get('/api/v1/products/tickets/')
    }
  }

})();