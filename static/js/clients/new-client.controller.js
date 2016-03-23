/**
* NewClientController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('NewClientController', NewClientController);

  NewClientController.$inject = ['$rootScope', '$scope', 'Clients'];

  /**
  * @namespace NewClientController
  */
  function NewClientController($rootScope, $scope, Clients) {
    var vm = this;

    vm.submit = submit;
    vm.makeSnapshot = makeSnapshot;
    vm.onSuccess = onSuccess;

    vm.list_matches = [];
    vm.matches_show = false;
    vm.search_client = search_client;
    vm.fdata = {gender: 0,
                avatar: 'data:image/jpg;base64,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',
              }

    function search_client() {
      Clients.exact_search(vm.fdata).then(clntSearchSuccessFn, clntSearchErrorFn);

      function clntSearchSuccessFn(data, status, headers, config) {
        if (data.data.length > 0) {
          vm.list_matches = data.data;
        } else {
          vm.list_matches = []
        };
      };

      function clntSearchErrorFn(data, status, headers, config) {
        console.log(data);
      };
    };

    vm.myChannel = {
        // the fields below are all optional
        video: null // Will reference the video element on success
      };
    var _video = vm.myChannel.video;

    /**
    * @name submit
    * @desc Create a new Client
    * @memberOf fcbp.client.controllers.NewClientController
    */
    function submit() {

      var numberPattern = /\d+/g;

      if (vm.fdata.mobile_form){
        var mobile = vm.fdata.mobile_form.match( numberPattern );
        vm.fdata.mobile = mobile.join("");
      } else {
        delete vm.fdata.mobile
      }

      if (vm.fdata.phone_str){
        var phone = vm.fdata.phone_str.match( numberPattern );
        vm.fdata.phone = phone.join("");
      } else {
        delete vm.fdata.phone
      }

      Clients.create(vm.fdata).then(createClientSuccessFn, createClientErrorFn);


      /**
      * @name createClientSuccessFn
      * @desc Show snackbar with success message
      */
      function createClientSuccessFn(data, status, headers, config) {
        console.log(data.data.id)
        console.log('Success! Client created.');
        window.location = '#/new-client-product/' + data.data.id + '/';
      }


      /**
      * @name createClientErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createClientErrorFn(data, status, headers, config) {
        console.log(data, status, headers, config)
        $rootScope.$broadcast('Client.created.error');
      }
    }

    function onSuccess() {
        // The video element contains the captured camera data
        _video = vm.myChannel.video;
    };

    /**
     * Make a snapshot of the camera data and show it in another canvas.
     */
    function makeSnapshot() {
      if (_video) {
          var patCanvas = document.querySelector('#snapshot');
          if (!patCanvas) return;


          patCanvas.width = _video.width;
          patCanvas.height = _video.height;
          var ctxPat = patCanvas.getContext('2d');

          var idata = getVideoData(0, 0, patCanvas.width, patCanvas.height);
          ctxPat.putImageData(idata, 0, 0);

          sendSnapshotToServer(patCanvas.toDataURL());
      }
    };

    var getVideoData = function getVideoData(x, y, w, h) {
        var hiddenCanvas = document.createElement('canvas');
        hiddenCanvas.width = _video.width;
        hiddenCanvas.height = _video.height;
        var ctx = hiddenCanvas.getContext('2d');
        ctx.drawImage(_video, 0, 0, _video.width, _video.height);
        return ctx.getImageData(x, y, w, h);
    };

    /**
     * This function could be used to send the image data
     * to a backend server that expects base64 encoded images.
     */
    var sendSnapshotToServer = function sendSnapshotToServer(imgBase64) {
        vm.fdata.avatar = imgBase64;
    };

  };

})();