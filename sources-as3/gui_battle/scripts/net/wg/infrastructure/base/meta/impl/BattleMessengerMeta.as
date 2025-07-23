package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.components.BattleUIDisplayable;
   import net.wg.gui.battle.views.battleMessenger.VO.BattleMessengerReceiverVO;
   import net.wg.gui.battle.views.battleMessenger.VO.BattleMessengerSettingsVO;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class BattleMessengerMeta extends BattleUIDisplayable
   {
       
      
      public var sendMessageToChannel:Function;
      
      public var focusReceived:Function;
      
      public var focusLost:Function;
      
      public var getToxicStatus:Function;
      
      public var onToxicButtonClicked:Function;
      
      public var onToxicPanelClosed:Function;
      
      private var _battleMessengerSettingsVO:BattleMessengerSettingsVO;
      
      private var _battleMessengerReceiverVO:BattleMessengerReceiverVO;
      
      private var _vectorBattleMessengerReceiverVO:Vector.<BattleMessengerReceiverVO>;
      
      public function BattleMessengerMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:BattleMessengerReceiverVO = null;
         if(this._battleMessengerSettingsVO)
         {
            this._battleMessengerSettingsVO.dispose();
            this._battleMessengerSettingsVO = null;
         }
         if(this._battleMessengerReceiverVO)
         {
            this._battleMessengerReceiverVO.dispose();
            this._battleMessengerReceiverVO = null;
         }
         if(this._vectorBattleMessengerReceiverVO)
         {
            for each(_loc1_ in this._vectorBattleMessengerReceiverVO)
            {
               _loc1_.dispose();
            }
            this._vectorBattleMessengerReceiverVO.splice(0,this._vectorBattleMessengerReceiverVO.length);
            this._vectorBattleMessengerReceiverVO = null;
         }
         super.onDispose();
      }
      
      public function sendMessageToChannelS(param1:int, param2:String) : Boolean
      {
         App.utils.asserter.assertNotNull(this.sendMessageToChannel,"sendMessageToChannel" + Errors.CANT_NULL);
         return this.sendMessageToChannel(param1,param2);
      }
      
      public function focusReceivedS() : void
      {
         App.utils.asserter.assertNotNull(this.focusReceived,"focusReceived" + Errors.CANT_NULL);
         this.focusReceived();
      }
      
      public function focusLostS() : void
      {
         App.utils.asserter.assertNotNull(this.focusLost,"focusLost" + Errors.CANT_NULL);
         this.focusLost();
      }
      
      public function getToxicStatusS(param1:String) : Object
      {
         App.utils.asserter.assertNotNull(this.getToxicStatus,"getToxicStatus" + Errors.CANT_NULL);
         return this.getToxicStatus(param1);
      }
      
      public function onToxicButtonClickedS(param1:String, param2:Number) : void
      {
         App.utils.asserter.assertNotNull(this.onToxicButtonClicked,"onToxicButtonClicked" + Errors.CANT_NULL);
         this.onToxicButtonClicked(param1,param2);
      }
      
      public function onToxicPanelClosedS(param1:String) : void
      {
         App.utils.asserter.assertNotNull(this.onToxicPanelClosed,"onToxicPanelClosed" + Errors.CANT_NULL);
         this.onToxicPanelClosed(param1);
      }
      
      public final function as_setupList(param1:Object) : void
      {
         var _loc2_:BattleMessengerSettingsVO = this._battleMessengerSettingsVO;
         this._battleMessengerSettingsVO = new BattleMessengerSettingsVO(param1);
         this.setupList(this._battleMessengerSettingsVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      public final function as_setReceiver(param1:Object, param2:Boolean) : void
      {
         var _loc3_:BattleMessengerReceiverVO = this._battleMessengerReceiverVO;
         this._battleMessengerReceiverVO = new BattleMessengerReceiverVO(param1);
         this.setReceiver(this._battleMessengerReceiverVO,param2);
         if(_loc3_)
         {
            _loc3_.dispose();
         }
      }
      
      public final function as_setReceivers(param1:Array, param2:int) : void
      {
         var _loc6_:BattleMessengerReceiverVO = null;
         var _loc3_:Vector.<BattleMessengerReceiverVO> = this._vectorBattleMessengerReceiverVO;
         this._vectorBattleMessengerReceiverVO = new Vector.<BattleMessengerReceiverVO>(0);
         var _loc4_:uint = param1.length;
         var _loc5_:int = 0;
         while(_loc5_ < _loc4_)
         {
            this._vectorBattleMessengerReceiverVO[_loc5_] = new BattleMessengerReceiverVO(param1[_loc5_]);
            _loc5_++;
         }
         this.setReceivers(this._vectorBattleMessengerReceiverVO,param2);
         if(_loc3_)
         {
            for each(_loc6_ in _loc3_)
            {
               _loc6_.dispose();
            }
            _loc3_.splice(0,_loc3_.length);
         }
      }
      
      protected function setupList(param1:BattleMessengerSettingsVO) : void
      {
         var _loc2_:String = "as_setupList" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
      
      protected function setReceiver(param1:BattleMessengerReceiverVO, param2:Boolean) : void
      {
         var _loc3_:String = "as_setReceiver" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc3_);
         throw new AbstractException(_loc3_);
      }
      
      protected function setReceivers(param1:Vector.<BattleMessengerReceiverVO>, param2:int) : void
      {
         var _loc3_:String = "as_setReceivers" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc3_);
         throw new AbstractException(_loc3_);
      }
   }
}
