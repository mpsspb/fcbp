/**
* Training
* @namespace fcbp.layout.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.services')
    .factory('Training', Training);

  Training.$inject = ['$http'];

  /**
  * @namespace Training
  * @returns {Factory}
  */
  function Training($http) {
    /**
    * @name Training
    * @desc The Factory to be returned
    */
    var Training = {
      create: create,
      list: list,
    };

    return Training;

    ////////////////////
    /**
    * @name create
    * @desc Create a new Training
    * @param {form data} by models of the new Training
    * @returns {Promise}
    * @memberOf fcbp.training.services.Training
    */
    function create(fdata) {
      return $http.post('/api/v1/products/training/', fdata
                        ).error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list() {
      return $http.get('/api/v1/products/training/')
    }
  }

})();