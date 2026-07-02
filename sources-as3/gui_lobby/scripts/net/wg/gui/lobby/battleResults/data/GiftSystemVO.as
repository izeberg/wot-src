package net.wg.gui.lobby.battleResults.data
{
   import net.wg.data.constants.Errors;
   import net.wg.data.daapi.base.DAAPIDataClass;
   import net.wg.utils.IAssertable;
   
   public class GiftSystemVO extends DAAPIDataClass
   {
      
      public static const STAMP_KEY:String = "stamp";
      
      public static const SPECIAL_STAMP_KEY:String = "specialStamp";
      
      public static const BLOCKED_PLAYERS_KEY:String = "blockedPlayers";
       
      
      public var isEnabled:Boolean = false;
      
      public var stamp:GiftStampVO = null;
      
      public var specialStamp:GiftStampVO = null;
      
      public var blockedPlayers:Vector.<int> = null;
      
      public var inSendProgressPlayer:int = -1;
      
      public var bannerTitle:String = "";
      
      private var _asserter:IAssertable;
      
      public function GiftSystemVO(param1:Object)
      {
         this._asserter = App.utils.asserter;
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         var _loc3_:Array = null;
         if(param1 == STAMP_KEY)
         {
            this.stamp = new GiftStampVO(param2);
            return false;
         }
         if(param1 == SPECIAL_STAMP_KEY)
         {
            this.specialStamp = new GiftStampVO(param2);
            return false;
         }
         if(param1 == BLOCKED_PLAYERS_KEY)
         {
            _loc3_ = param2 as Array;
            this._asserter.assertNotNull(_loc3_,Errors.CANT_NULL);
            this.fillBlockedPlayers(_loc3_);
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         if(this.stamp != null)
         {
            this.stamp.dispose();
            this.stamp = null;
         }
         if(this.specialStamp != null)
         {
            this.specialStamp.dispose();
            this.specialStamp = null;
         }
         if(this.blockedPlayers != null)
         {
            this.blockedPlayers.splice(0,this.blockedPlayers.length);
            this.blockedPlayers = null;
         }
         super.onDispose();
      }
      
      private function fillBlockedPlayers(param1:Array) : void
      {
         var _loc2_:int = 0;
         var _loc3_:int = 0;
         if(param1)
         {
            _loc2_ = param1.length;
            this.blockedPlayers = new Vector.<int>(_loc2_);
            _loc3_ = 0;
            while(_loc3_ < _loc2_)
            {
               this.blockedPlayers[_loc3_] = param1[_loc3_];
               _loc3_++;
            }
         }
      }
      
      public function isPlayerBlocked(param1:int) : Boolean
      {
         var _loc2_:int = 0;
         var _loc3_:int = this.blockedPlayers.length;
         _loc2_ = 0;
         while(_loc2_ < _loc3_)
         {
            if(param1 == this.blockedPlayers[_loc2_])
            {
               return true;
            }
            _loc2_++;
         }
         return false;
      }
   }
}
