package net.wg.gui.lobby.personalMissions.components
{
   import flash.display.InteractiveObject;
   import flash.display.Sprite;
   import net.wg.data.constants.LobbyMetrics;
   import net.wg.gui.lobby.personalMissions.components.operationsHeader.OperationTitleInfo;
   import net.wg.gui.lobby.personalMissions.data.OperationDataVO;
   import net.wg.gui.lobby.personalMissions.data.OperationTitleVO;
   import net.wg.gui.lobby.personalMissions.events.OperationEvent;
   import net.wg.infrastructure.base.meta.IPMOldOperationsMeta;
   import net.wg.infrastructure.base.meta.impl.PMOldOperationsMeta;
   import net.wg.infrastructure.interfaces.IViewStackExContent;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.motion.Tween;
   
   public class PMOldOperations extends PMOldOperationsMeta implements IPMOldOperationsMeta, IViewStackExContent
   {
      
      private static const INVALID_OPERATIONS:String = "invalidOperations";
      
      private static const INVALID_TITLE:String = "invalidTitle";
      
      private static const HEADER_TOP_POSITION_MAX:int = 85;
      
      private static const HEADER_TOP_POSITION_MIN:int = 55;
      
      private static const CONTENT_TOP_POSITION_MIN:int = 300;
      
      private static const HEIGHT_BREAK_POINT:int = 812;
      
      private static const PAGE_HEIGHT_STATE_TALL:String = "stateTall";
      
      private static const PAGE_HEIGHT_STATE_SHORT:String = "stateShort";
      
      private static const FADE_IN_TIME:uint = 500;
       
      
      public var operationInfo:OperationTitleInfo = null;
      
      public var content:AllOperationsContent = null;
      
      public var bg:Sprite = null;
      
      private var _titleVo:OperationTitleVO = null;
      
      private var _operations:Vector.<OperationDataVO> = null;
      
      private var _pageHeightState:String = "";
      
      private var _showTween:Tween = null;
      
      public function PMOldOperations()
      {
         super();
         visible = false;
         alpha = 0;
      }
      
      private static function calcPageHeightState(param1:Number) : String
      {
         return param1 >= HEIGHT_BREAK_POINT ? PAGE_HEIGHT_STATE_TALL : PAGE_HEIGHT_STATE_SHORT;
      }
      
      override public function setSize(param1:Number, param2:Number) : void
      {
         _originalWidth = param1;
         _originalHeight = param2;
         setActualSize(param1,param2);
         setActualScale(1,1);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.content.addEventListener(OperationEvent.CLICK,this.onContentOperationClickHandler);
         this.operationInfo.addEventListener(OperationEvent.INFO_BTN_CLICK,this.onOperationInfoBtnClickHandler);
      }
      
      override protected function onBeforeDispose() : void
      {
         this.operationInfo.removeEventListener(OperationEvent.INFO_BTN_CLICK,this.onOperationInfoBtnClickHandler);
         this.content.removeEventListener(OperationEvent.CLICK,this.onContentOperationClickHandler);
         super.onBeforeDispose();
      }
      
      override protected function onDispose() : void
      {
         if(this._showTween)
         {
            this._showTween.dispose();
            this._showTween = null;
         }
         this.operationInfo.dispose();
         this.operationInfo = null;
         this._operations.length = 0;
         this._operations = null;
         this.content.dispose();
         this.content = null;
         this.bg = null;
         this._titleVo = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._titleVo && isInvalid(INVALID_TITLE))
         {
            this.operationInfo.update(this._titleVo);
         }
         if(this._operations && isInvalid(INVALID_OPERATIONS))
         {
            this.content.setOperations(this._operations);
         }
         if(isInvalid(InvalidationType.SIZE))
         {
            this.updateSize();
         }
      }
      
      override protected function setOperations(param1:Vector.<OperationDataVO>) : void
      {
         this._operations = param1;
         invalidate(INVALID_OPERATIONS);
      }
      
      override protected function setTitle(param1:OperationTitleVO) : void
      {
         this._titleVo = param1;
         invalidate(INVALID_TITLE);
      }
      
      public function canShowAutomatically() : Boolean
      {
         return true;
      }
      
      public function getComponentForFocus() : InteractiveObject
      {
         return this.content;
      }
      
      public function setActive(param1:Boolean) : void
      {
         if(param1)
         {
            if(!this._showTween)
            {
               this._showTween = new Tween(FADE_IN_TIME,this,{"alpha":1});
            }
            else
            {
               this._showTween.reset();
               this._showTween.paused = false;
            }
         }
         else
         {
            this._showTween.paused = true;
            alpha = 0;
         }
      }
      
      public function update(param1:Object) : void
      {
      }
      
      private function updateSize() : void
      {
         var _loc1_:String = null;
         _loc1_ = calcPageHeightState(height);
         if(this._pageHeightState != _loc1_)
         {
            this._pageHeightState = _loc1_;
            this.updateDependentComponents(this._pageHeightState);
         }
         var _loc2_:int = width >> 1;
         var _loc3_:int = height >> 1;
         this.content.x = _loc2_;
         this.content.y = _loc1_ == PAGE_HEIGHT_STATE_SHORT ? Number(CONTENT_TOP_POSITION_MIN + (App.appHeight - LobbyMetrics.MIN_STAGE_HEIGHT >> 1)) : Number(_loc3_);
         this.operationInfo.x = _loc2_;
         this.operationInfo.y = Math.min(HEADER_TOP_POSITION_MIN + (App.appHeight - LobbyMetrics.MIN_STAGE_HEIGHT >> 1),HEADER_TOP_POSITION_MAX);
         this.bg.width = width;
         this.bg.height = height + LobbyMetrics.LOBBY_MESSENGER_HEIGHT;
      }
      
      private function updateDependentComponents(param1:String) : void
      {
         this.operationInfo.fontSize = param1 == PAGE_HEIGHT_STATE_TALL ? int(OperationTitleInfo.HEADER_FONT_BIG) : int(OperationTitleInfo.HEADER_FONT_SMALL);
      }
      
      private function onOperationInfoBtnClickHandler(param1:OperationEvent) : void
      {
         showInfoS();
      }
      
      private function onContentOperationClickHandler(param1:OperationEvent) : void
      {
         onOperationClickS(param1.pmType,param1.id);
      }
   }
}
