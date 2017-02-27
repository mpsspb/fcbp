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
      active_list: active_list,
      update: update,
      active: active,
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

    function list() {
      return $http.get('/api/v1/products/training/')
    }

    function active(uid) {
      return $http.post('/api/v1/products/training/' + uid + '/active/')
    }

    function active_list() {
      return $http.get('/api/v1/products/training/active_list/')
    }

    function update(id, fdata) {
      return $http.put('/api/v1/products/training/' + id + '/', fdata
                        ).error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
  }

})();