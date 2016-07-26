/**
* CardText
* @namespace fcbp.layout.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.services')
    .factory('CardText', CardText);

  CardText.$inject = ['$http'];

  /**
  * @namespace CardText
  * @returns {Factory}
  */
  function CardText($http) {
    /**
    * @name CardText
    * @desc The Factory to be returned
    */
    var CardText = {
      list: list,
      update: update,
    };

    return CardText;

    ////////////////////
    /**
    **/
    function list() {
      return $http.get('/api/v1/products/cardtext/')
    }

    function update(id, fdata) {
      return $http.put('/api/v1/products/cardtext/' + id + '/', fdata
                        ).error(function(data, status, headers, config) {
                          console.log(data)
                        });
    }
  }

})();