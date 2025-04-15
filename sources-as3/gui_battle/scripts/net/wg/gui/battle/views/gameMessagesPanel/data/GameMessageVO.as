package net.wg.gui.battle.views.gameMessagesPanel.data
{
   import net.wg.data.constants.generated.GAME_MESSAGES_CONSTS;
   import net.wg.data.daapi.base.DAAPIDataClass;
   import net.wg.gui.battle.interfaces.IGameMessageVO;
   
   public class GameMessageVO extends DAAPIDataClass implements IGameMessageVO
   {
      
      private static const SECONDS_TO_MILLISECONDS:Number = 1000;
      
      private static const MSG_DATA:String = "msgData";
       
      
      protected var _messageType:String = "";
      
      protected var _priority:int = -1;
      
      protected var _length:Number = -1;
      
      protected var _msgData:BaseGameMessageVO = null;
      
      protected var _cachedMsgData:Object = null;
      
      public function GameMessageVO(param1:Object)
      {
         super(param1);
         this.convertMsgData();
      }
      
      override public function toString() : String
      {
         return "MessagesVO " + this.messageType + " " + this.priority + " " + this.length;
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         if(param1 == MSG_DATA)
         {
            this._cachedMsgData = param2;
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         if(this.msgData)
         {
            this.msgData.dispose();
            this.msgData = null;
         }
         this._cachedMsgData = null;
         super.onDispose();
      }
      
      protected function convertMsgData() : void
      {
         switch(this.messageType)
         {
            case GAME_MESSAGES_CONSTS.WIN:
            case GAME_MESSAGES_CONSTS.DEFEAT:
            case GAME_MESSAGES_CONSTS.DRAW:
               this.msgData = new EndGameMessageVO(this._cachedMsgData);
               break;
            case GAME_MESSAGES_CONSTS.TIME_REMAINING_POSITIVE:
            case GAME_MESSAGES_CONSTS.TIME_REMAINING:
               this.msgData = new BaseGameMessageVO(this._cachedMsgData);
               break;
            default:
               this.msgData = new BaseGameMessageVO(this._cachedMsgData);
         }
         this._cachedMsgData = null;
      }
      
      public function get duration() : int
      {
         return this.length * SECONDS_TO_MILLISECONDS;
      }
      
      public function get messageType() : String
      {
         return this._messageType;
      }
      
      public function set messageType(param1:String) : void
      {
         this._messageType = param1;
      }
      
      public function get length() : Number
      {
         return this._length;
      }
      
      public function set length(param1:Number) : void
      {
         this._length = param1;
      }
      
      public function get priority() : int
      {
         return this._priority;
      }
      
      public function set priority(param1:int) : void
      {
         this._priority = param1;
      }
      
      public function get msgData() : BaseGameMessageVO
      {
         return this._msgData;
      }
      
      public function set msgData(param1:BaseGameMessageVO) : void
      {
         this._msgData = param1;
      }
   }
}
