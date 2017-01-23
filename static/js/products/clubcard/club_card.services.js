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
      update: update,
      use: use,
      use_update: use_update,
      use_get: use_get,
      use_del: use_del,
      use_exit: use_exit,
      guest: guest,
      personal: personal,
      fitness: fitness,
      prolongation: prolongation,
      prolongation_del: prolongation_del,
      freeze: freeze,
      freeze_del: freeze_del,
      active: active,
      active_list: active_list,
      archive_list: archive_list,
      archive_client_list: archive_client_list,
      archive_reopen: archive_reopen,
      archive_purge_credits: archive_purge_credits,
      archive_get: archive_get,
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

    function archive_list(uid) {
      return $http.get('/api/v1/clients/archive/clubcard/')
    }

    function archive_client_list(uid) {
      return $http.get('/api/v1/clients/archive/clubcard/'+ uid + '/client/')
    }

    function archive_reopen(uid) {
      return $http.post('/api/v1/clients/archive/clubcard/'+ uid + '/reopen/')
    }

    function archive_purge_credits(uid) {
      return $http.post('/api/v1/clients/archive/clubcard/'+ uid + '/purge_credits/')
    }

    function archive_get(uid) {
      return $http.get('/api/v1/clients/archive/clubcard/' + uid + '/')
    }

    function update(uid, fdata) {
      return $http.put('/api/v1/products/club_cards/' + uid + '/', fdata)
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

    function use_update(uid, fdata) {
      return $http.put('/api/v1/clients/useclubcard/' + uid + '/',  fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }

    function use_get(uid) {
      return $http.get('/api/v1/clients/useclubcard/' + uid + '/')
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }

    function use_del(uid) {
      return $http.delete('/api/v1/clients/useclubcard/' + uid + '/')
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
      if (fdata.id > 0) {
        return $http.put('/api/v1/clients/personalclubcard/' + fdata.id + '/',  fdata)
                    .error(function(data, status, headers, config) {
                            console.log(data)
                          });
      } else {
        return $http.post('/api/v1/clients/personalclubcard/',  fdata)
                    .error(function(data, status, headers, config) {
                            console.log(data)
                          });
      }
    }

    function fitness(fdata) {
      if (fdata.id > 0) {
        return $http.put('/api/v1/clients/fitness/' + fdata.id + '/',  fdata)
                    .error(function(data, status, headers, config) {
                            console.log(data)
                          });
      } else {
        return $http.post('/api/v1/clients/fitness/',  fdata)
                    .error(function(data, status, headers, config) {
                            console.log(data)
                          });
      }
    }

    function prolongation(fdata) {
      return $http.post('/api/v1/clients/prolongation/',  fdata)
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }

    function prolongation_del(uid) {
      return $http.delete('/api/v1/clients/prolongation/' + uid + '/')
                  .error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }

    function freeze(uid, fdata) {
      return $http.post('/api/v1/clients/clubcard/' + uid + '/freeze/', fdata)
    }


    function freeze_del(uid) {
      // delete freeze club card
      return $http.delete('/api/v1/clients/freezecc/' + uid + '/')
    }

  }

})();