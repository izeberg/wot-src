package net.wg.gui.lobby.battleResults.components.giftSystem
{
   import flash.events.MouseEvent;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.gui.lobby.battleResults.data.GiftSystemVO;
   import net.wg.gui.lobby.battleResults.data.TeamMemberItemVO;
   import net.wg.gui.lobby.battleResults.event.GiftSystemSendEvent;
   import net.wg.infrastructure.base.UIComponentEx;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class GiftSystemButtons extends UIComponentEx
   {
       
      
      public var sendButton:GiftSystemSendButton = null;
      
      public var sendSpecialButton:GiftSystemSendButton = null;
      
      protected var _teamMemberItemVO:TeamMemberItemVO = null;
      
      protected var _giftSystemVO:GiftSystemVO = null;
      
      public function GiftSystemButtons()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.sendButton.visible = this.sendSpecialButton.visible = false;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.sendButton.mouseEnabledOnDisabled = this.sendSpecialButton.mouseEnabledOnDisabled = true;
         this.sendButton.addEventListener(ButtonEvent.CLICK,this.onGiftSendButtonClickHandler);
         this.sendButton.addEventListener(MouseEvent.ROLL_OVER,this.onGiftSendButtonRollOverHandler);
         this.sendButton.addEventListener(MouseEvent.ROLL_OUT,this.onGiftSendButtonRollOutHandler);
         this.sendSpecialButton.addEventListener(ButtonEvent.CLICK,this.onGiftSendButtonClickHandler);
         this.sendSpecialButton.addEventListener(MouseEvent.ROLL_OVER,this.onGiftSendButtonRollOverHandler);
         this.sendSpecialButton.addEventListener(MouseEvent.ROLL_OUT,this.onGiftSendButtonRollOutHandler);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            if(this._teamMemberItemVO && this._giftSystemVO)
            {
               this.updateButtonStates();
            }
            else
            {
               this.sendButton.visible = this.sendSpecialButton.visible = false;
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this.sendButton.removeEventListener(ButtonEvent.CLICK,this.onGiftSendButtonClickHandler);
         this.sendButton.removeEventListener(MouseEvent.ROLL_OVER,this.onGiftSendButtonRollOverHandler);
         this.sendButton.removeEventListener(MouseEvent.ROLL_OUT,this.onGiftSendButtonRollOutHandler);
         this.sendButton.dispose();
         this.sendButton = null;
         this.sendSpecialButton.removeEventListener(ButtonEvent.CLICK,this.onGiftSendButtonClickHandler);
         this.sendSpecialButton.removeEventListener(MouseEvent.ROLL_OVER,this.onGiftSendButtonRollOverHandler);
         this.sendSpecialButton.removeEventListener(MouseEvent.ROLL_OUT,this.onGiftSendButtonRollOutHandler);
         this.sendSpecialButton.dispose();
         this.sendSpecialButton = null;
         this._teamMemberItemVO = null;
         this._giftSystemVO = null;
         super.onDispose();
      }
      
      public function setTeamMemberData(param1:TeamMemberItemVO) : void
      {
         this._teamMemberItemVO = param1;
         invalidateData();
      }
      
      public function setGiftSystemData(param1:GiftSystemVO) : void
      {
         this._giftSystemVO = param1;
         invalidateData();
      }
      
      private function updateButtonStates() : void
      {
         this.sendSpecialButton.visible = this._giftSystemVO.specialStamp.count > Values.ZERO;
         this.sendButton.visible = !this.sendSpecialButton.visible;
         var _loc1_:Boolean = this._giftSystemVO.inSendProgressPlayer == this._teamMemberItemVO.playerId;
         this.sendButton.loading = this.sendSpecialButton.loading = _loc1_;
         if(_loc1_)
         {
            return;
         }
         var _loc2_:Boolean = this._giftSystemVO.stamp.count + this._giftSystemVO.specialStamp.count > Values.ZERO;
         var _loc3_:Boolean = this._giftSystemVO.isPlayerBlocked(this._teamMemberItemVO.playerId);
         var _loc4_:Boolean = this._giftSystemVO.inSendProgressPlayer != Values.DEFAULT_INT;
         var _loc5_:Boolean = this._giftSystemVO.isEnabled && !_loc4_ && _loc2_ && !_loc3_;
         this.sendButton.enabled = this.sendSpecialButton.enabled = _loc5_;
      }
      
      private function onGiftSendButtonRollOverHandler(param1:MouseEvent) : void
      {
         var _loc2_:GiftSystemSendButton = null;
         if(this._teamMemberItemVO && this._giftSystemVO && this._giftSystemVO.isPlayerBlocked(this._teamMemberItemVO.playerId))
         {
            _loc2_ = param1.target as GiftSystemSendButton;
            if(_loc2_ && !_loc2_.enabled && !_loc2_.loading)
            {
               App.toolTipMgr.showWulfTooltip(TOOLTIPS_CONSTANTS.BIRTHDAY_GIFT_SYSTEM_DISABLED_PLAYER,this._teamMemberItemVO.playerId);
            }
         }
      }
      
      private function onGiftSendButtonRollOutHandler(param1:MouseEvent) : void
      {
         App.toolTipMgr.hide();
      }
      
      private function onGiftSendButtonClickHandler(param1:ButtonEvent) : void
      {
         var _loc2_:String = null;
         param1.stopPropagation();
         if(this._teamMemberItemVO && this._giftSystemVO)
         {
            _loc2_ = param1.target == this.sendButton ? this._giftSystemVO.stamp.name : this._giftSystemVO.specialStamp.name;
            dispatchEvent(new GiftSystemSendEvent(this._teamMemberItemVO.playerId,_loc2_));
         }
      }
   }
}
