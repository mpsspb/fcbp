/**
* ClubCard
* @namespace fcbp.layout.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.services')
    .factory('ClubCard', ClubCard);

  ClubCard.$inject = ['$http'];

  /**
  * @namespace ClubCard
  * @returns {Factory}
  */
  function ClubCard($http) {
    /**
    * @name ClubCard
    * @desc The Factory to be returned
    */
    var ClubCard = {
      create: create,
      list: list,
      get: get,
      use: use,
      use_exit: use_exit,
      guest: guest,
      personal: personal,
      fitness: fitness,
      prolongation: prolongation,
      freeze: freeze,
      active: active,
      active_list: active_list,
    };

    return ClubCard;

    ////////////////////
    /**
    * @name create
    * @desc Create a new ClubCard
    * @param {array} The form data of the new ClubCard
    * @returns {Promise}
    * @memberOf fcbp.layout.services.ClubCard
    */
    function create(fdata) {
      return $http.post('/api/v1/products/club_cards/', fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
    /**
    **/
    function list() {
      return $http.get('/api/v1/products/club_cards/')
    }

    function active_list() {
      return $http.get('/api/v1/products/club_cards/active_list/')
    }

    function get(uid) {
      return $http.get('/api/v1/clients/clubcard/' + uid + '/')
    }

    function active(uid) {
      return $http.post('/api/v1/products/club_cards/' + uid + '/active/')
    }

    function guest(uid, fdata) {
      return $http.post('/api/v1/clients/clubcard/' + uid + '/guest/', fdata)
    }

    function use(fdata) {
      return $http.post('/api/v1/clients/useclubcard/',  fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }

    function use_exit(fdata) {
      return $http.post('/api/v1/clients/useclubcard/exit/',  fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }

    function personal(fdata) {
      return $http.post('/api/v1/clients/personalclubcard/',  fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }

    function fitness(fdata) {
      return $http.post('/api/v1/clients/fitness/',  fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }

    function prolongation(fdata) {
      return $http.post('/api/v1/clients/prolongation/',  fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }

    function freeze(uid, fdata) {
      return $http.post('/api/v1/clients/clubcard/' + uid + '/freeze/', fdata)
    }

  }

})();