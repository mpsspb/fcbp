/**
* Authentication
* @namespace fcbp.auth.services
*/
(function () {
  'use strict';

  angular
    .module('fcbp.auth.services')
    .factory('Authentication', Authentication);

  Authentication.$inject = ['$localStorage', '$http'];

  /**
  * @namespace Authentication
  * @returns {Factory}
  */
  function Authentication($localStorage, $http) {
    /**
    * @name Authentication
    * @desc The Factory to be returned
    */
    var Authentication = {
      getAuthenticatedAccount: getAuthenticatedAccount,
      isAuthenticated: isAuthenticated,
      logout: logout,
      unauthenticate: unauthenticate
    };

    return Authentication;

    ////////////////////

    /**
     * @name logout
     * @desc Try to log the user out
     * @returns {Promise}
     * @memberOf fcbp.authentication.services.Authentication
     */
    function logout() {
      return $http.post('/api/v1/users/logout/')
        .then(logoutSuccessFn, logoutErrorFn);

      /**
       * @name logoutSuccessFn
       * @desc Unauthenticate and redirect to index with page reload
       */
      function logoutSuccessFn(data, status, headers, config) {
        Authentication.unauthenticate();
        window.location = '/';
      }

      /**
       * @name logoutErrorFn
       * @desc Log "Epic failure!" to the console
       */
      function logoutErrorFn(data, status, headers, config) {
        console.error('Epic failure!');
      }
    }
    
    /**
     * @name getAuthenticatedAccount
     * @desc Return the currently authenticated account
     * @returns {object|undefined} Account if authenticated, else `undefined`
     * @memberOf fcbp.authentication.services.Authentication
     */
    function getAuthenticatedAccount() {
      if ($localStorage.user) {
        return JSON.parse($localStorage.user);
      }
      return
    }

    /**
     * @name isAuthenticated
     * @desc Check if the current user is authenticated
     * @returns {boolean} True is user is authenticated, else false.
     * @memberOf fcbp.authentication.services.Authentication
     */
    function isAuthenticated() {
      return !!$localStorage.user;
    }

    /**
     * @name unauthenticate
     * @desc Delete the cookie where the user object is stored
     * @returns {undefined}
     * @memberOf fcbp.authentication.services.Authentication
     */
    function unauthenticate() {
      $localStorage.$reset();
    }

  }

})();