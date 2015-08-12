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
  }

})();